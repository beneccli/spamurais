import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="max-w-lg mx-auto mt-24 bg-white dark:bg-zinc-700 border rounded-lg shadow-lg border-zinc-100 dark:border-zinc-600">

      <div class="px-8 py-6 text-lg font-bold">Notifications</div>

      <div class="px-8 mb-6">
        <div class="flex w-full rounded-md bg-zinc-100 dark:bg-zinc-800">
          <a class="block w-1/3 m-1 font-light text-center"
              routerLink="/alerts"
              routerLinkActive="bg-white rounded-md shadow dark:bg-zinc-700 font-medium"
              ariaCurrentWhenActive="page"
          >Alerts</a>
          <a class="block w-1/3 m-1 font-light text-center"
              routerLink="/important"
              routerLinkActive="bg-white rounded-md shadow dark:bg-zinc-700 font-medium"
              ariaCurrentWhenActive="page"
          >Important</a>
          <a class="block w-1/3 m-1 font-light text-center"
              routerLink="/archived"
              routerLinkActive="bg-white rounded-md shadow dark:bg-zinc-700 font-medium"
              ariaCurrentWhenActive="page"
          >Archived</a>
        </div>
      </div>

      <router-outlet></router-outlet>

    </div>
  `
})
export class AppComponent {
  title = 'spamurais-ui';
}
