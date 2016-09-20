from Tkinter import *
from svm_handler import SVMHandler
from mail import send_email
import threading
import tkMessageBox

__author__ = 'stas'


def run_gui():
    svm_handler = SVMHandler()

    def thread_starter(func, arguments):
        """ 
        This method receives a function and a tuple of arguments. Starts the function  
        in a thread. daemon = True so the thread will stop when the main thread finishes (window closed)
        """
        t = threading.Thread(target=func, args=arguments)
        t.daemon = True
        t.start()

    def activate_train():
        """
        invoking the training in a thread
        """
        thread_starter(svm_handler.train, ())

    def activate_test():
        """
        invoking the testing in a thread, checking if the classifier is created
        """
        if not svm_handler.is_classifier_exists():
            tkMessageBox.showinfo("Support Vector Machine",
                                  "Please, teach the SVM before testing it "
                                  "(start training and wait until its finished)")
        else:
            thread_starter(svm_handler.test, ())

    def send_mail():
        """
        invoking the email sending in a thread, checking if the the error percentage was calculated
        """
        if svm_handler.error_percentage == -1:
            tkMessageBox.showinfo("Support Vector Machine",
                                  "Please, test the SVM before sending the result "
                                  "(start testing and wait until its finished)")
        else:
            thread_starter(send_email, (svm_handler.error_percentage,))

    """
    creating the GUI, using Tkinter, setting configurations of the root,
    creating a frame that holds: 3 buttons inside a 1 row and 3 columns grid .
    """
    root = Tk()
    root.title("SVM GUI")
    # Here you need to set the frame, grid, row and column configurations of the root.
    mainframe = Frame(root)
    mainframe.pack()

    e1 = Button(mainframe, text="Start Training", command=activate_train)
    e2 = Button(mainframe, text="Start Testing", command=activate_test)
    e3 = Button(mainframe, text="Send results to Email", command=send_mail)

    e1.grid(row=0, column=0)
    e2.grid(row=0, column=1)
    e3.grid(row=0, column=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
