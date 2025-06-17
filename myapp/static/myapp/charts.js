
         var areaChart = new CanvasJS.Chart("areaChart", {
         animationEnabled: true,
         exportEnabled: true,
         axisX: {
         lineColor: "rgba(0, 0, 0, .125)",
         labelFontColor: "rgba(0, 0, 0, .5)",
         tickColor: "rgba(0, 0, 0, .125)",
         minimum: 0,
         maximum: 11
         },
         axisY: {
         gridColor: "rgba(0, 0, 0, .125)",
         lineColor: "rgba(0, 0, 0, .125)",
         labelFontColor: "rgba(0, 0, 0, .5)",
         tickColor: "rgba(0, 0, 0, .125)",
         includeZero: true
         },
         toolTip: {
         shared: true
         },
         data: [{
         type: "splineArea",
         name: "Sessions",
         fillOpacity: 0.25,
         markerSize: 10,
         markerBorderThickness: 2,
         markerBorderColor: "white",        
         color: "rgb(2, 117, 216)",
         dataPoints: {{ area_data | safe }}
         }]
         });
         areaChart.render();
         
         // -- Bar Chart
         var columnChart = new CanvasJS.Chart("columnChart", {
         animationEnabled: true,
         exportEnabled: true,
         axisX: {
         lineColor: "rgba(0, 0, 0, .125)",
         labelFontColor: "rgba(0, 0, 0, .5)",
         tickColor: "rgba(0, 0, 0, .125)"
         },
         axisY: {
         gridColor: "rgba(0, 0, 0, .125)",
         lineColor: "rgba(0, 0, 0, .125)",
         labelFontColor: "rgba(0, 0, 0, .5)",
         tickColor: "rgba(0, 0, 0, .125)",
         includeZero: true
         },
         toolTip: {
         shared: true
         },
         data: [{
         type: "column",
         color: "rgb(2,117,216)",
         name: "Revenue",
         yValueFormatString: "$#,###",
         dataPoints: {{ column_data | safe }}
         }]
         });
         columnChart.render();
         
         // -- Pie Chart
         var pieChart = new CanvasJS.Chart("pieChart", {
         animationEnabled: true,
         exportEnabled: true,
         legend: {
         verticalAlign: "top"
         },
         data: [{
         type: "pie",
         showInLegend: true,
         dataPoints: {{ pie_data | safe }}
         }]
         });
         pieChart.render();
