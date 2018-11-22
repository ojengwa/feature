function FeatureRequest(data) {
    this.id = ko.observable(data.id);
    this.title = ko.observable(data.title);
    this.description = ko.observable(data.description);
}

function FeatureRequestListViewModel() {
    var that = this;
    that.feature_requests = ko.observableArray([]);
    that.newFeatureRequestTitle = ko.observable();
    that.newFeatureRequestDesc = ko.observable();

    that.addFeatureRequest = function () {
        that.save();
        that.newFeatureRequestTitle("");
        that.newFeatureRequestDesc("");
    };

    $.getJSON('/feature_requests', function (taskModels) {
        var feature_request = $.map(taskModels.feature_requests, function (ele) {
            return new FeatureRequest(ele);
        });
        that.feature_requests(feature_request);
    });

    that.save = function () {
        return $.ajax({
            url: '/feature_requests/new',
            contentType: 'application/json',
            type: 'POST',
            data: JSON.stringify({
                'title': that.newFeatureRequestTitle(),
                'description': that.newFeatureRequestDesc()
            }),
            success: function (data) {
                console.log("Pushing to feature_requests array");
                that.feature_requests.push(new FeatureRequest({ title: data.title, description: data.description, id: data.id }));
                return;
            },
            error: function () {
                return console.log("Failed");
            }
        });
    };
}

ko.applyBindings(new FeatureRequestListViewModel());