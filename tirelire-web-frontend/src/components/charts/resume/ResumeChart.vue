<script setup>

  import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'

  const lineChart = {
    id: 'line',
    type: 'line',
    data: {
      labels: ['January','February','March','April','May','June','July'],
      datasets: [
        {
          label: 'Account 1',
          data: [812, 538, 54, 776, 904, 514, 816],
          borderColor: "#03830E",
          backgroundColor: "#03830E",
          cubicInterpolationMode: 'linear',
          tension: 0.4
        },
        {
          label: 'Account 2',
          data: [656, 279, 65, 966, 686, 726, 1069],
          borderColor: "#59AB60",
          backgroundColor: "#59AB60",
          cubicInterpolationMode: 'linear',
          tension: 0.4
        },
      ]
    },
    options: {
      maintainAspectRatio: false,
      scales: {
        y: {
          display: false,
        }
      }
    }
  }
  </script>

<template>
  <div>
    <vue3-chart-js :id="lineChart.id" :type="lineChart.type" :data="lineChart.data" :options="lineChart.options"/>
  </div>
</template>