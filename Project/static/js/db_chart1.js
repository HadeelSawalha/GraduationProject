
    // Load google charts
            google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    // Draw the chart and set the chart values
    function drawChart(pnumonia,normal) {
    console.log(pnumonia);
        console.log(normal);
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Pneumonia',pnumonia],
            ['Normal',normal],


        ]);
        console.log(data);
// console.log({{numpnumonia}});
          //   console.log({{numnormal}});
        // Optional; add a title and set the width and height of the chart{{pnumonia}}{{Normal}}{{numpnumonia}}{{numnormal}}
        var options = { 'width': 470, 'height': 400 };

        // Display the chart inside the <div> element with id="piechart"
        var chart = new google.visualization.PieChart(document.getElementById('PatientStatistics1'));
        chart.draw(data, options);
    }
