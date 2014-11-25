/**
 * Created by haoxu on 14-9-6.
 */

define(["knockout", "appViewModel", "domReady!"], function(ko, appViewModel) {
    ko.applyBindings(new appViewModel.nameHandlerModel());
});
