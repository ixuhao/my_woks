/**
 * Created by haoxu on 14-9-6.
 */

requirejs.config({
    "baseUrl": "scripts/lib",
    "paths": {
        "app": "../app",
        "knockout": "knockout-3.2.0",
        "appViewModel": "../app/appViewModel",
        "domReady": "domReady"
    }
});

requirejs(["app/main"]);
