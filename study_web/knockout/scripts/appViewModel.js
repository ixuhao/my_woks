/**
 *
 * Created by xuhao on 8/25/14.
 */

define(['knockout-3.2.0'], function(ko) {
    return function appViewModel() {
        this.availableMeals = [
            {mealName: 'Standard', description: 'Dry crusts of bread', extraCost: 0},
            {mealName: 'Premium', description: 'Fresh bread with cheese', extraCost: 9.95},
            {mealName: 'Deluxe', description: 'Caviar and vintage Dr Pepper', extraCost: 18.50}
        ];
        this.firstName = ko.observable('Bert');
        this.firstNameCaps = ko.pureComputed(function(){
            return this.firstName().toUpperCase();
        }, this);
        this.chosenMeal = ko.observable(this.availableMeals[0]);
    };
});

