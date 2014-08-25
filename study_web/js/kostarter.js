/**
 *
 * Created by xuhao on 8/25/14.
 */

requirejs.config({
        paths: {
            knockout: "knockout-3.2.0"
        }
});

requirejs(['knockout'], function (ko) {
        var availableMeals = [
            { mealName: 'Standard', description: 'Dry crusts of bread', extraCost: 0},
            { mealName: 'Premium', description: 'Fresh bread with cheese', extraCost: 9.95},
            { mealName: 'Deluxe', description: 'Caviar and vintange Dr Pepper', extraCost: 18.50}
        ];

        var viewModel = {
//             we'll populate this in a moment
        };

        ko.applyBindings(viewModel);

});
