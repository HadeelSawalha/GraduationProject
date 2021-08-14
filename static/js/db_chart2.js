
    // Load google charts
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    // Draw the chart and set the chart values
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Female',50],
            ['Male', 50],



        ]);

        // Optional; add a title and set the width and height of the chart{{male}} {{Female}}{{numfemale}}{{nummale}}
        var options = { 'width': 470, 'height': 400 };

        // Display the chart inside the <div> element with id="piechart"
        var chart = new google.visualization.PieChart(document.getElementById('PatientStatistics2'));
        chart.draw(data, options);
    }
