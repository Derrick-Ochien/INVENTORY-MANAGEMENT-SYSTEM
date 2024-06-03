from tkinter import *
from tkinter import messagebox
import datetime

class Application():
    def __init__(self, master):
        self.master = master
        self.master.title("MAMA DERRICK STORE")

        # Frame to hold all widgets
        self.frame = Frame(master, bg='pink')
        self.frame.pack(expand=True, fill=BOTH)

        # Left frame for product entry and receipt
        self.left_frame = Frame(self.frame, bg='pink')
        self.left_frame.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)

        # Right frame for total bill and payment
        self.right_frame = Frame(self.frame, bg='pink')
        self.right_frame.pack(side=RIGHT, padx=20, pady=20, fill=BOTH, expand=True)

        # Heading
        self.heading = Label(self.left_frame, text="MAMA DERRICK STORE", font=('ALGERIAN', 30, 'bold'), fg='Black', bg='pink')
        self.heading.pack(pady=10)

        # Date
        self.date = datetime.datetime.now().date()
        self.date_label = Label(self.left_frame, text="Date: " + str(self.date), font=('Calibri', 18), fg='black', bg='pink')
        self.date_label.pack(pady=10)

        # Product Entry
        self.product_label = Label(self.left_frame, text="Product Name:", font=('Calibri', 16), fg='Black', bg='pink')
        self.product_label.pack(pady=5)
        self.product_name = StringVar()
        self.product_entry = Entry(self.left_frame, textvariable=self.product_name, font=('Calibri', 16), bg='lightblue', width=25)
        self.product_entry.pack(pady=5)

        self.quantity_label = Label(self.left_frame, text="Quantity:", font=('Calibri', 16), fg='Black', bg='pink')
        self.quantity_label.pack(pady=5)
        self.quantity = IntVar()
        self.quantity_entry = Entry(self.left_frame, textvariable=self.quantity, font=('Calibri', 16), bg='lightblue', width=25)
        self.quantity_entry.pack(pady=5)

        self.price_label = Label(self.left_frame, text="Price:", font=('Calibri', 16), fg='Black', bg='pink')
        self.price_label.pack(pady=5)
        self.price = DoubleVar()
        self.price_entry = Entry(self.left_frame, textvariable=self.price, font=('Calibri', 16), bg='lightblue', width=25)
        self.price_entry.pack(pady=5)

        self.add_button = Button(self.left_frame, text="Add Item", width=15, height=2, bg='green', font=('Calibri', 16), command=self.add_item)
        self.add_button.pack(pady=10)

        # Receipt
        self.receipt_label = Label(self.left_frame, text="Receipt", font=('Calibri', 20, 'bold', 'underline'), fg='Black', bg='pink')
        self.receipt_label.pack(pady=10)
        self.receipt_text = Text(self.left_frame, height=20, width=40, font=('Calibri', 16))
        self.receipt_text.pack(pady=5)

        # Total Bill
        self.total_bill_label = Label(self.right_frame, text="Total Bill:", font=('Calibri', 18), fg='Black', bg='pink')
        self.total_bill_label.pack(pady=5)
        self.total_bill = DoubleVar()
        self.total_bill_entry = Entry(self.right_frame, textvariable=self.total_bill, font=('Calibri', 16), bg='lightblue', state='readonly', width=20)
        self.total_bill_entry.pack(pady=5)

        # Discount Offered
        self.discount_label = Label(self.right_frame, text="Discount Offered:", font=('Calibri', 18), fg='Black', bg='pink')
        self.discount_label.pack(pady=5)
        self.discount = DoubleVar()
        self.discount_entry = Entry(self.right_frame, textvariable=self.discount, font=('Calibri', 16), bg='lightblue', width=20)
        self.discount_entry.pack(pady=5)

        # Payment
        self.payment_label = Label(self.right_frame, text="Payment:", font=('Calibri', 18), fg='Black', bg='pink')
        self.payment_label.pack(pady=5)
        self.payment = DoubleVar()
        self.payment_entry = Entry(self.right_frame, textvariable=self.payment, font=('Calibri', 16), bg='lightblue', width=20)
        self.payment_entry.pack(pady=5)

        self.calculate_button = Button(self.right_frame, text="Calculate", width=15, height=2, bg='green', font=('Calibri', 16), command=self.calculate)
        self.calculate_button.pack(pady=10)

        # Difference
        self.difference_label = Label(self.right_frame, text="Difference:", font=('Calibri', 18), fg='Black', bg='pink')
        self.difference_label.pack(pady=5)
        self.difference = DoubleVar()
        self.difference_entry = Entry(self.right_frame, textvariable=self.difference, font=('Calibri', 16), bg='lightblue', state='readonly', width=20)
        self.difference_entry.pack(pady=5)

        # Reset Button
        self.reset_button = Button(self.right_frame, text="Reset", width=15, height=2, bg='red', font=('Calibri', 16), command=self.reset)
        self.reset_button.pack(pady=10)

        # Close Button
        self.close_button = Button(self.right_frame, text="Close", width=15, height=2, bg='red', font=('Calibri', 16), command=master.quit)
        self.close_button.pack(pady=5)

        # Initialize total bill
        self.total_bill.set(0.0)

        # Transaction ID and time
        self.transaction_id = f"TX{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.transaction_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Initialize receipt header
        self.receipt_text.insert(END, f"Store: MAMA DERRICK STORE\n")
        self.receipt_text.insert(END, f"Transaction ID: {self.transaction_id}\n")
        self.receipt_text.insert(END, f"Date: {self.date}\n")
        self.receipt_text.insert(END, f"Time: {self.transaction_time}\n")
        self.receipt_text.insert(END, "============================\n")

    def add_item(self):
        product = self.product_name.get()
        quantity = self.quantity.get()
        price = self.price.get()
        total_price = quantity * price
        self.receipt_text.insert(END, f"Product: {product}\nQuantity: {quantity}\nPrice: {price}\nTotal Price: {total_price}\n")
        self.receipt_text.insert(END, "----------------------------\n")
        self.total_bill.set(self.total_bill.get() + total_price)

    def calculate(self):
        payment = self.payment.get()
        total_bill = self.total_bill.get()
        discount = self.discount.get()
        net_total = total_bill - discount
        difference = payment - net_total
        self.difference.set(difference)

        # Update receipt with discount and net total
        self.receipt_text.insert(END, f"Discount: {discount}\n")
        self.receipt_text.insert(END, f"Net Total: {net_total}\n")
        self.receipt_text.insert(END, f"Payment: {payment}\n")
        self.receipt_text.insert(END, f"Difference: {difference}\n")
        self.receipt_text.insert(END, "============================\n")

    def reset(self):
        self.product_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.receipt_text.delete(1.0, END)
        self.total_bill.set(0.0)
        self.discount.set(0.0)
        self.payment.set(0.0)
        self.difference.set(0.0)
        self.transaction_id = f"TX{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.transaction_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.receipt_text.insert(END, f"Store: MAMA DERRICK STORE\n")
        self.receipt_text.insert(END, f"Transaction ID: {self.transaction_id}\n")
        self.receipt_text.insert(END, f"Date: {self.date}\n")
        self.receipt_text.insert(END, f"Time: {self.transaction_time}\n")
        self.receipt_text.insert(END, "============================\n")

root = Tk()
app = Application(root)
root.mainloop()
