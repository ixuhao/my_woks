/**
 * Created by xuhao on 8/26/14.
 */

define(['knockout-3.2.0', 'customBidingHandlers/hasForcus'], function(ko) {
    return function appViewModel() {
        ko.bindingHandlers.hasFocus = {
            init: function(),
            update: function()
        };
        this.editingName = ko.observable();
    };
});
