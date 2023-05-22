<template>
  <div>
    <h2>Добавить матч</h2>
    <form @submit.prevent="handleSubmit">
      <p>
        <label for="player1">Первый игрок</label>:
        <select id="player1" v-model="player1Id" required>
          <option v-for="player in players" :key="player.id" :value="player.id">{{ player.name }} {{ player.surname }}</option>
        </select>
      </p>
      <p>
        <label for="player2">Второй игрок</label>:
        <select id="player2" v-model="player2Id" required>
          <option v-for="player in filteredPlayers" :key="player.id" :value="player.id">{{ player.name }} {{ player.surname }}</option>
        </select>
      </p>
      <p>
        <label for="player2">Результат</label>:
        <select id="result" v-model="result" required>
          <option value="First won">Победа первого</option>
          <option value="Second won">Победа второго</option>
          <option value="Tie">Ничья</option>
        </select>
      </p>
      <button type="submit">Создать</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      player1Id: null,
      player2Id: null,
      result: null,
      players: [],
    };
  },
  async created() {
    await this.fetchPlayers()
  },
  methods: {
    async fetchPlayers() {
      try {
        const response = await this.$http.get('players');
        this.players = response.data
      }
      catch (error) {
        console.error(error)
      }
    },
    async handleSubmit() {
      const gameData = {
        player1_id: this.player1Id,
        player2_id: this.player2Id,
        result: this.result
      }
      try {
        const response = await this.$http.post('games', gameData)
        console.log(response)
      }
      catch (error) {
        console.error(error)
      }
    }
  },
  computed: {
    filteredPlayers() {
      return this.players.filter(player => player.id !== this.player1Id)
    }
  }
};
</script>