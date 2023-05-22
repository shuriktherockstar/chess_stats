<template>
  <div>
    <h2>Список матчей</h2>
    <table>
      <thead>
        <tr>
          <th>Матч</th>
          <th>Исход</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="game in games" :key="game.id">
          <td>{{ getPlayerName(game.player1_id) + ' - ' + getPlayerName(game.player2_id) }}</td>
          <td>{{ getResult(game.result) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      games: [],
      players: [],
    };
  },
  async created() {
    await this.fetchGames();
    await this.fetchPlayers();
  },
  methods: {
    async fetchGames() {
      try {
        const response = await this.$http.get('games');
        this.games = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchPlayers() {
      try {
        const response = await this.$http.get('players');
        this.players = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    getPlayerName(playerId) {
      const player = this.players.find(player => player.id === playerId);
      return player ? `${player.name} ${player.surname}` : '';
    },
    getResult(result) {
      if (result === 'First won') {
        return 'Победа первого'
      }
      else if (result === 'Second won') {
        return 'Победа второго'
      }
      else {
        return 'Ничья'
      }
    }
  },
};
</script>