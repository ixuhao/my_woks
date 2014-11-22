/**
 *
 * Created by haoxu on 14-9-6.
 */

define(["knockout"], function(ko){
    return {
        nameHandlerModel:
            function () {
                this.firstName = ko.observable("Bert");
                this.secondName = ko.observable("Bertington");
                this.fullName = ko.computed(function () {
                    return this.firstName() + " " + this.secondName();
                }, this);
                this.capitalizeLastName = function () {
                    var currentVal = this.secondName();
                    this.secondName(currentVal.toUpperCase());
                };
            }
    }
});
