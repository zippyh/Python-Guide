# Zippyh
# This program runs best in PyCharm
import kivy

kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

widgets = []
page = [' ']


class Main_Layout(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_Layout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.next = Button(text='next')
        self.next.bind(on_press=self.next_press)
        self.home = Button(text='home')
        self.home.bind(on_press=self.home_press)
        self.welcome_label = (
            Label(text="This is a guide to using some of the most important commands in python. " + '\n'
                                                                                                    "Click any "
                                                                                                    "of the buttons below to continue."))
        self.add_widget(self.welcome_label)
        self.for_loops = Button(text="How to code and use for loops")
        self.for_loops.bind(on_press=self.for_loop_press)
        self.add_widget(self.for_loops)
        self.while_loops = Button(text="How to code and use while loops")
        self.while_loops.bind(on_press=self.while_loop_press)
        self.add_widget(self.while_loops)
        self.lists = Button(text="How to code and use lists")
        self.lists.bind(on_press=self.lists_press)
        self.add_widget(self.lists)
        self.procedure = Button(text="How to code and use procedures")
        self.procedure.bind(on_press=self.procedure_press)
        self.add_widget(self.procedure)
        widgets.append(self.welcome_label)
        widgets.append(self.for_loops)
        widgets.append(self.while_loops)
        widgets.append(self.lists)
        widgets.append(self.procedure)

    def remove_widgets(self):
        for i in range(len(widgets)):
            self.remove_widget(widgets[i])
        widgets.clear()

    def for_loops_p2(self):
        self.for_loops5 = Label(text='For loops can also be used in tandem with lists.' + '\n' + 'Two common ways '
                                                                                                 'that they can '
                                                                                                 'appear are '
                                                                                                 'shown below:')
        self.add_widget(self.for_loops5)
        self.for_loops6 = Label(text='1: for i, item in enumerate(list):' + '\n' + '2: for i in range(len(list)):')
        self.add_widget(self.for_loops6)
        self.for_loops7 = Label(
            text='In the fist for loop the i represents the number of iterations, ' + '\n' + 'the item '
                                                                                             'represents the item in '
                                                                                             'the list with the index '
                                                                                             'equal to i, ' + '\n' +
                 'and the enumerate(list) command turns the list into an enumerable object ' + '\n' +
                 'which is then used to cause the loop to repeat for each item in the list.' + '\n' +
                 'The second for loop is almost the same as a basic for loop, the only ' + '\n' +
                 'difference is the len(list) command. The len(list) command returns the ' + '\n' +
                 'length of an object, in this case that is the list.')
        self.add_widget(self.for_loops7)
        self.add_widget(self.home)
        widgets.append(self.for_loops5)
        widgets.append(self.for_loops6)
        widgets.append(self.for_loops7)
        widgets.append(self.home)

    def while_loops_p2(self):
        self.while_loops5 = Label(text='One of the most common ways for loops are used is with if statements.' '\n'
                                       'They can appear as any of the ones shown below:')
        self.add_widget(self.while_loops5)
        self.while_loops6 = Label(text='while i == 0:' '\n' 'while i != 0:' '\n' 'while i > 0:' '\n' 'while i < 0:')
        self.add_widget(self.while_loops6)
        self.while_loops7 = Label(
            text='In all of these for loops the i just represents any variable and can be ' '\n'
                 'swapped out with any other variable in the program. When using a loop ' '\n'
                 'like this it will repeat as long as a certain condition is true. For ' '\n'
                 'example if I have a for loop that says while i == 0: it will repeat until ' '\n'
                 'i no longer equals 0.')
        self.add_widget(self.while_loops7)
        self.add_widget(self.home)
        widgets.append(self.while_loops5)
        widgets.append(self.while_loops6)
        widgets.append(self.while_loops7)
        widgets.append(self.home)

    def lists_p2(self):
        self.lists5 = Label(text='List are mutable, which means you can change the items stored in it without ' '\n'
                                 'changing the identity of the list. Below is an example of how to change a list: ')
        self.add_widget(self.lists5)
        self.lists6 = Label(text='list = ["this", "is", "a", "list"]' '\n' 'list[1] = "hi"' '\n' 'The list would '
                                 'then equal ["this", "hi", "a", "list"]')
        self.add_widget(self.lists6)
        self.lists7 = Label(
            text='When changing a specific item in the list it is important to write the name of ' '\n'
                 'the list and then in brackets the index of the item you want to replace. Then ' '\n'
                 'you just use an equal sign to set what you want the item to be replaced with.')
        self.add_widget(self.lists7)
        self.add_widget(self.home)
        widgets.append(self.lists5)
        widgets.append(self.lists6)
        widgets.append(self.lists7)
        widgets.append(self.home)

    def procedure_p2(self):
        self.procedure5 = Label(
            text='Procedures can also be used with something called a parameter. A parameter ' '\n'
                 'is placed within the parentheses at the end of the procedure, and can have ' '\n'
                 'varying affects. Below is an example of a procedure being used ' '\n' 'with a'
                 ' parameter:')
        self.add_widget(self.procedure5)
        self.procedure6 = Label(
            text='def this_is_a_procedure(num):' '\n' '    for i in range(num):' '\n' '      print("hi")'
                 '\n' 'this_is_a_procedure(3)' '\n' 'The output would then be:' '\n' 'hi' '\n' 'hi' '\n' 'hi')
        self.add_widget(self.procedure6)
        self.procedure7 = Label(
            text='The parameter, "num" is used to determine the number of times the program ' '\n'
                 'will print "hi". The value for num is determined in the call to the ' '\n'
                 'procedure. In this case the value of num was set to 3 so the program ' '\n'
                 'printed "hi" three times.')
        self.add_widget(self.procedure7)
        self.add_widget(self.home)
        widgets.append(self.procedure5)
        widgets.append(self.procedure6)
        widgets.append(self.procedure7)
        widgets.append(self.home)

    def after_next(self, num):
        self.remove_widgets()
        if num == 1:
            self.for_loops_p2()
        elif num == 2:
            self.while_loops_p2()
        elif num == 3:
            self.lists_p2()
        elif num == 4:
            self.procedure_p2()

    def home_press(self, instance):
        self.remove_widgets()
        self.next = Button(text='next')
        self.next.bind(on_press=self.next_press)
        self.home = Button(text='home')
        self.home.bind(on_press=self.home_press)
        self.welcome_label = (
            Label(text="This is a guide to using some of the most important commands in python. " + '\n'
                                                                                                    "Click any "
                                                                                                    "of the buttons below to continue."))
        self.add_widget(self.welcome_label)
        self.for_loops = Button(text="How to code and use for loops")
        self.for_loops.bind(on_press=self.for_loop_press)
        self.add_widget(self.for_loops)
        self.while_loops = Button(text="How to code and use while loops")
        self.while_loops.bind(on_press=self.while_loop_press)
        self.add_widget(self.while_loops)
        self.lists = Button(text="How to code and use lists")
        self.lists.bind(on_press=self.lists_press)
        self.add_widget(self.lists)
        self.procedure = Button(text="How to code and use procedures")
        self.procedure.bind(on_press=self.procedure_press)
        self.add_widget(self.procedure)
        widgets.append(self.welcome_label)
        widgets.append(self.for_loops)
        widgets.append(self.while_loops)
        widgets.append(self.lists)
        widgets.append(self.procedure)

    def next_press(self, instance):
        if page[0] == 'for loops':
            self.after_next(1)
        elif page[0] == 'while loops':
            self.after_next(2)
        elif page[0] == 'lists':
            self.after_next(3)
        elif page[0] == 'procedure':
            self.after_next(4)

    def for_loop_press(self, instance):
        self.remove_widgets()
        self.for_loops1 = (Label(text='A for loop is a basic loop that repeats a set number of times.'))
        self.add_widget(self.for_loops1)
        self.for_loops2 = (Label(text='A for loop can appear like this:'))
        self.add_widget(self.for_loops2)
        self.for_loops3 = (Label(text='for i in range(x)'))
        self.add_widget(self.for_loops3)
        self.for_loops4 = (Label(text='In a for loop like this i is variable that represents the number of times the '
                                      'loop has repeated,' + '\n' + 'and x is the number of times the loop will '
                                                                    'repeat.'))
        self.add_widget(self.for_loops4)
        self.add_widget(self.next)
        self.add_widget(self.home)
        widgets.append(self.for_loops1)
        widgets.append(self.for_loops2)
        widgets.append(self.for_loops3)
        widgets.append(self.for_loops4)
        widgets.append(self.next)
        widgets.append(self.home)
        page[0] = 'for loops'

    def while_loop_press(self, instance):
        self.remove_widgets()
        self.while_loops1 = Label(text='A while loop is a loop that can repeat an infinite number of times, or until '
                                       'a certain condition is met.')
        self.add_widget(self.while_loops1)
        self.while_loops2 = Label(text='A while loop can appear like this:')
        self.add_widget(self.while_loops2)
        self.while_loops3 = Label(text='While True:')
        self.add_widget(self.while_loops3)
        self.while_loops4 = Label(
            text='In a while loop the the loop will repeat as long as a certain condition is ' '\n'
                 'true. Since True will always be true this loop will repeat forever.')
        self.add_widget(self.while_loops4)
        self.add_widget(self.next)
        self.add_widget(self.home)
        widgets.append(self.while_loops1)
        widgets.append(self.while_loops2)
        widgets.append(self.while_loops3)
        widgets.append(self.while_loops4)
        widgets.append(self.next)
        widgets.append(self.home)
        page[0] = 'while loops'

    def lists_press(self, instance):
        self.remove_widgets()
        self.lists1 = Label(
            text='Lists are a basic way of storing information in Python. Lists are useful because ' '\n'
                 'information can be stored and extracted from lists very easily.')
        self.add_widget(self.lists1)
        self.lists2 = Label(text='An example of creating a list is below:')
        self.add_widget(self.lists2)
        self.lists3 = Label(text='list = ["this", "is", "a", "list"]')
        self.add_widget(self.lists3)
        self.lists4 = Label(
            text='The word list at the beginning, "list" is the name of the list. The list its self ' '\n'
                 'is stored in the brackets, each item in the list has an index starting at 0 and ' '\n'
                 'continuing until the last item in the list. The list can consist of letters and ' '\n'
                 'numbers at the same time')
        self.add_widget(self.lists4)
        self.add_widget(self.next)
        self.add_widget(self.home)
        widgets.append(self.lists1)
        widgets.append(self.lists2)
        widgets.append(self.lists3)
        widgets.append(self.lists4)
        widgets.append(self.next)
        widgets.append(self.home)
        page[0] = 'lists'

    def procedure_press(self, instance):
        self.remove_widgets()
        self.procedure1 = Label(text='Procedures are one of the most helpful commands in Python. A procedure ' '\n'
                                     'functions by first defining the the procedure. The procedure can then be ' '\n'
                                     'called upon an unlimited number of times.')
        self.add_widget(self.procedure1)
        self.procedure2 = Label(text='Procedures in Python usually look something like this:')
        self.add_widget(self.procedure2)
        self.procedure3 = Label(text='def this_is_a_procedure():' '\n' '    for i in range(4):' '\n' '      print("hi")'
                                     '\n' 'this_is_a_procedure()' '\n' 'The output would then be:' '\n' 'hi' '\n' 'hi' '\n' 'hi')
        self.add_widget(self.procedure3)
        self.procedure4 = Label(
            text='The first line gives the procedure its name with two parentheses at the end, ' '\n'
                 'like this "()". Code can then be inputted below. The procedure can then be ' '\n'
                 'called by typing the name of the procedure, followed by two parentheses')
        self.add_widget(self.procedure4)
        self.add_widget(self.next)
        self.add_widget(self.home)
        widgets.append(self.procedure1)
        widgets.append(self.procedure2)
        widgets.append(self.procedure3)
        widgets.append(self.procedure4)
        widgets.append(self.next)
        widgets.append(self.home)
        page[0] = 'procedure'


class ActionApp(App):
    def build(self):
        return Main_Layout()


if __name__ == '__main__':
    ActionApp().run()