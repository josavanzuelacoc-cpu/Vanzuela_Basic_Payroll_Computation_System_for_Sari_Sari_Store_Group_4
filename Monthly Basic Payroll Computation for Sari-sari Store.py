# Monthly Basic Payroll Computation for Sari-sari Store

def compute_payroll():
    employees = []
    num_employees = int(input("Enter number of employees: "))
    
    for i in range(num_employees):
        print(f"\nEmployee {i+1}:")
        name = input("Enter employee name: ")
        hours_worked = float(input("Enter hours worked this month: "))
        hourly_rate = float(input("Enter hourly rate (in PHP): "))
        deduction_rate = float(input("Enter deduction rate (as decimal, e.g., 0.1 for 10%): "))
        
        gross_pay = hours_worked * hourly_rate
        deductions = gross_pay * deduction_rate
        net_pay = gross_pay - deductions
        
        employees.append({
            "name": name,
            "hours": hours_worked,
            "rate": hourly_rate,
            "gross": gross_pay,
            "deductions": deductions,
            "net": net_pay
        })
    
    # Display summary
    print("\n=== Monthly Payroll Summary ===")
    total_gross = 0
    total_net = 0
    for emp in employees:
        print(f"\n{emp['name']}:")
        print(f"  Hours: {emp['hours']}")
        print(f"  Rate: {emp['rate']} PHP")
        print(f"  Gross Pay: {emp['gross']} PHP")
        print(f"  Deductions: {emp['deductions']} PHP")
        print(f"  Net Pay: {emp['net']} PHP")
        total_gross += emp['gross']
        total_net += emp['net']
    
    print(f"\nTotal Gross Payroll: {total_gross} PHP")
    print(f"Total Net Payroll: {total_net} PHP")

if _name_ == "_main_":
    compute_payroll()
