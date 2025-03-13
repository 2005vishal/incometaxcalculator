class IncomeTaxCalculator:
    def surcharge_tax(self, total_amount, tax, tax_regime):
        surcharge_rate = 0

        if total_amount > 5000000 and total_amount <= 10000000:
            surcharge_rate = 0.10
        elif total_amount > 10000000 and total_amount <= 20000000:
            surcharge_rate = 0.15
        elif total_amount > 20000000 and total_amount <= 50000000:
            surcharge_rate = 0.20
        elif total_amount > 50000000:
            surcharge_rate = 0.37 if tax_regime == "old" else 0.25  # Old regime has 37%, new has 25%

        return tax * surcharge_rate  # Apply surcharge on tax, not income

    def old_tax_regime_calculator(self, amount,deduction):
        ic = amount
        Deduction = deduction

        taxable_income = ic - (50000 + Deduction)  # Income after standard deduction

        if taxable_income <= 500000:
            tax, surcharge, cess, total_tax = 0,0,0,0
            return  taxable_income, tax, surcharge, cess, total_tax


        tax = 0
        if taxable_income > 1000000:
            tax = 250000 * 0.05 + 500000 * 0.20 + (taxable_income - 1000000) * 0.30
        elif taxable_income > 500000:
            tax = 250000 * 0.05 + (taxable_income - 500000) * 0.20
        else:
            tax = (taxable_income - 250000) * 0.05

        surcharge = self.surcharge_tax(taxable_income, tax, tax_regime="old")

        tax_with_surcharge = tax + surcharge
        cess = tax_with_surcharge * 0.04  # Cess (4%) on tax + surcharge
        total_tax = tax_with_surcharge + cess

        return taxable_income, tax, surcharge, cess, total_tax

    def new_tax_regime_calculator(self, amount,deduction):
        ic = amount
        Deduction = deduction
        taxable_income = ic - (75000+Deduction)

        if taxable_income <= 1200000:
            tax, surcharge, cess, total_tax = 0,0,0,0
            return taxable_income, tax, surcharge, cess, total_tax


        tax = 0
        if taxable_income > 2400000:
            tax = 400000 * 0.05 + 400000 * 0.10 + 400000 * 0.15 + 400000 * 0.20 + 400000 * 0.25 + (
                        taxable_income - 2400000) * 0.30
        elif taxable_income > 2000000:
            tax = 400000 * 0.05 + 400000 * 0.10 + 400000 * 0.15 + 400000 * 0.20 + (taxable_income - 2000000) * 0.25
        elif taxable_income > 1600000:
            tax = 400000 * 0.05 + 400000 * 0.10 + 400000 * 0.15 + + (taxable_income - 1600000) * 0.20
        elif taxable_income > 1200000:
            tax = 400000 * 0.05 + 400000 * 0.10 + (taxable_income - 1200000) * 0.15
        elif taxable_income > 800000:
            tax = 400000 * 0.05 + (taxable_income - 800000) * 0.10
        elif taxable_income > 400000:
            tax = (taxable_income - 400000) * 0.05


        surcharge = self.surcharge_tax(taxable_income, tax, tax_regime="new")


        tax_with_surcharge = tax + surcharge
        cess = tax_with_surcharge * 0.04
        total_tax = tax_with_surcharge + cess

        return taxable_income, tax, surcharge, cess, total_tax


# Run the tax calculator
# tax_calculator = IncomeTaxCalculator()
# print(tax_calculator.new_tax_regime_calculator(700000,deduction=0))