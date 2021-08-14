
    window.onload = function () {

        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            title: {
                text: "Our System Vs Real Life for Pneumonia "
            },
            axisY: {
                title: "Our System",
                titleFontColor: "#4F81BC",
                lineColor: "#4F81BC",
                labelFontColor: "#4F81BC",
                tickColor: "#4F81BC"
            },
            axisY2: {
                title: "Real Life",
                titleFontColor: "#C0504E",
                lineColor: "#C0504E",
                labelFontColor: "#C0504E",
                tickColor: "#C0504E"
            },
            toolTip: {
                shared: true
            },
            legend: {
                cursor: "pointer",
                itemclick: toggleDataSeries
            },
            data: [{
                type: "column",
                name: "Our System",
                legendText: "Our System",
                showInLegend: true,
                dataPoints: [
                    { label: "Time of x-ray", y: 1.00 },
                    { label: "Cost of  patient", y: 120.00 },
                    { label: "Time of  patient", y: 3.00 },
                    { label: "Number of patient /hour", y: 20.00 },
                    
                ]
            },
            {
                type: "column",
                name: "Real Life",
                legendText: "Real Life",
                axisYType: "secondary",
                showInLegend: true,
                dataPoints: [
                    { label: "Time of x-ray", y: 30.00 },
                    { label: "Cost of  patient", y: 500.00 },
                    { label: "Time of  patient", y: 60.00 },
                    { label: "Number of patient /hour", y: 2.00 },
                    
                ]
            }]
        });
        chart.render();

        function toggleDataSeries(e) {
            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                e.dataSeries.visible = false;
            }
            else {
                e.dataSeries.visible = true;
            }
            chart.render();
        }

    }
