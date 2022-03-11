<script>
  import AccountCard from '@/components/account-card/AccountCard'
  import NewAccountCard from '@/components/account-card/NewAccountCard'
  import ResumeChart from '@/components/charts/resume/ResumeChart'

  export default {
    components: {
      AccountCard,
      NewAccountCard,
      ResumeChart
    },
    data () {
      return {
        name: 'Renaud',
        accounts: [
          {
            "id": "id123",
            "name": "Account 1"
          },
          {
            "id": "idabc",
            "name": "Account 2"
          },
        ]
      }
    }
  }
</script>

<template>
  <div>
    <h1>Welcome {{ name }} !</h1>
    <div class="section">
      <h1>Resume</h1>
      <div class="chart">
        <ResumeChart />
      </div>
    </div>
    <div class="section">
      <h1>Account(s)</h1>
      <ul class="accounts">
        <li 
          v-for="account in accounts" 
          :key="account.id"
        >
          <AccountCard :name="account.name" />
        </li>
        <li>
          <NewAccountCard />
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
  .section {
    position: relative;
    display: inline;
  }
  .section h1 {
    margin-left: 16px;
    text-align: left;
    border-bottom: 2px solid rgb(90, 160, 76);
    color: rgb(90, 160, 76);
  }
  .section h1:hover{
    color: rgb(37, 102, 0);
    border-bottom: 2px solid rgb(37, 102, 0);
    transition: all 0.5s;
  }
  .accounts li{
    list-style-type: none;
    float: left;
  }
  .chart {  
    max-height: 240px;
    padding-top: .5%;
    position: relative;
  }
  .ResumeChart {
    position: relative;
  }
</style>
