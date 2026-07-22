def disp_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date}")

disp_invoice("Priyanka" , 120.09, "01/02/26")