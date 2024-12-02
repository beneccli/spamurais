import { CommonModule } from '@angular/common';
import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="fixed inset-x-0 inset-y-24">
      <div
        class="max-w-lg mx-auto h-full overflow-auto bg-white dark:bg-zinc-700 border rounded-lg shadow-lg border-zinc-100 dark:border-zinc-600"
        #scrollContainer
        (scroll)="calculateIfMenuTabsIsFixed($event)"
      >

        <div class="px-8 pt-6 text-lg font-bold">Notifications</div>

        <div
          class="px-8 py-6 sticky top-0 backdrop-blur-3xl dark:backdrop-blur-xl border-b"
          #stickyElement
          [class.border-transparent]="!isFixed"
          [class.border-zinc-200]="isFixed"
          [class.dark:border-zinc-600]="isFixed"
        >
          <div class="flex w-full rounded-md bg-zinc-100 dark:bg-zinc-800">
            <a class="block flex-1 m-1 font-light text-center"
              routerLink="/alerts"
              routerLinkActive="bg-white rounded-md shadow dark:bg-zinc-700 font-medium"
              ariaCurrentWhenActive="page"
            >Notifications</a>
            <a class="block flex-1 m-1 font-light text-center"
              routerLink="/important"
              routerLinkActive="bg-white rounded-md shadow dark:bg-zinc-700 font-medium"
              ariaCurrentWhenActive="page"
            >Status</a>
          </div>
        </div>

        <router-outlet></router-outlet>

      </div>
    </div>
  `
})
export class AppComponent {
  title = 'spamurais-ui';
  @ViewChild('scrollContainer') scrollContainer!: ElementRef;
  @ViewChild('stickyElement') stickyElement!: ElementRef;
  isFixed = false;

  calculateIfMenuTabsIsFixed(_: Event) {
    const scrollContainer = this.scrollContainer.nativeElement as HTMLElement;
    const stickyElement = this.stickyElement.nativeElement as HTMLElement;

    // Get the scrollable container's top position
    const containerRect = scrollContainer.getBoundingClientRect();
    const stickyRect = stickyElement.getBoundingClientRect();

    // Check if the sticky element's top position matches the container's top
    this.isFixed = stickyRect.top <= containerRect.top + 1;
  }
}
