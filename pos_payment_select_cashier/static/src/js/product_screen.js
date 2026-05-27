odoo.define("pos_payment_select_cashier.ProductScreen", function (require) {
    "use strict";

    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const SelectCashierMixin = require("pos_hr.SelectCashierMixin");

    const PosPaymentSelectCashierProductScreen = (ProductScreen_) =>
        class extends SelectCashierMixin(ProductScreen_) {
            async _onClickPay() {
                if (this.env.pos.config.module_pos_hr) {
                    const employee = await this._selectPaymentCashier();
                    if (!employee) {
                        return;
                    }
                    this.env.pos.set_cashier(employee);
                }
                return super._onClickPay(...arguments);
            }

            async _selectPaymentCashier() {
                const currentCashier = this.env.pos.get_cashier();
                const employeesList = this.env.pos.employees.map((employee) => {
                    return {
                        id: employee.id,
                        item: employee,
                        label: employee.name,
                        isSelected: currentCashier && employee.id === currentCashier.id,
                    };
                });
                const {confirmed, payload: employee} = await this.showPopup(
                    "SelectionPopup",
                    {
                        title: this.env._t("Change Cashier"),
                        list: employeesList,
                    }
                );

                if (!confirmed || !employee) {
                    return;
                }
                if (
                    !employee.pin ||
                    (currentCashier && employee.id === currentCashier.id)
                ) {
                    return employee;
                }
                return this.askPin(employee);
            }
        };

    Registries.Component.extend(ProductScreen, PosPaymentSelectCashierProductScreen);

    return ProductScreen;
});
