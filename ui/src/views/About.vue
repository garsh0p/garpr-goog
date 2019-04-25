<template>
  <div>
    <h1 class="display-2">FAQ</h1>
    <v-card>
      <v-card-text>

        <h2 class="headline">What rating system does GAR PR use?</h2>
        <p class="body-1">Trueskill by Microsoft.</p>

        <h2 class="headline">Where can I find out more about how TrueSkill works?</h2>
        <p class="body-1">Trueskill is a ranking system developed by Microsoft that is used for ranking players in many of their online Xbox Live titles. Check out the articles below to find out more about how Trueskill works:</p>
        <ul>
          <li><a href="http://research.microsoft.com/en-us/projects/trueskill/">Microsoft Research - Trueskill Ranking System</a></li>
          <li><a href="http://www.moserware.com/2010/03/computing-your-skill.html">Moserware - Computing Your Skill</a></li>
          <li><a href="https://trueskill.org/">Trueskill Python implementation (the one used by GAR PR)</a></li>
        </ul>
        <p class="body-1">

        <h2 class="headline">What tournament programs do you support?</h2>
        <p class="body-1">Challonge and SmashGG.</p>

        <h2 class="headline">How do you handle inactive players?</h2>
        <p class="body-1">A region determines activity criteria, which are X tournaments in the past Y days. If a player becomes inactive they become hidden from the rankings list. They will still maintain the same rating they had before they became inactive. Once they enter enough tournaments to become active again, their old rating will be used to calculate their new rating and they will reappear on the rankings. Note that there is no rating decay of any kind.</p>

        <h2 class="headline">Do you take into account the set score (for example, 2-0 vs 2-1)?</h2>
        <p class="body-1">No, only the match result (win or loss) is recorded.</p>
        <iframe src='https://gfycat.com/ifr/HappyMinorAnnashummingbird' frameborder='0' scrolling='no' allowfullscreen width='640' height='404'></iframe>
      </v-card-text>
    </v-card>
  </div>
</template>
