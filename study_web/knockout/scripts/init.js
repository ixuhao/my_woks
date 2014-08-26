//require(['knockout-3.2.0', 'appViewModel', 'domReady!'], function(ko, appViewModel) {
require(['knockout-3.2.0', 'appViewModel'], function(ko, appViewModel) {
    ko.applyBindings(new appViewModel());
});
