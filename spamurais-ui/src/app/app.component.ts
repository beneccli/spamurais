import { CommonModule } from '@angular/common';
import { AfterViewInit, ChangeDetectorRef, Component, ElementRef, HostListener, OnDestroy, ViewChild } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { BehaviorSubject, debounceTime, Subject } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div
      class="fixed inset-x-0 top-24"
      [class.bottom-24]="isContainerMaxHeightReached"
    >
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
export class AppComponent implements AfterViewInit, OnDestroy {
  title = 'spamurais-ui';
  @ViewChild('scrollContainer') scrollContainer!: ElementRef;
  @ViewChild('stickyElement') stickyElement!: ElementRef;
  isFixed = false;
  isContainerMaxHeightReached = false;
  isContainerMaxHeightReached$ = new Subject<boolean>();

  private resizeObserver!: ResizeObserver;

  constructor(private cdr: ChangeDetectorRef) {
    this.isContainerMaxHeightReached$
      .pipe(debounceTime(50))
      .subscribe((value) => {
        this.isContainerMaxHeightReached = value;
      });
    this.isContainerMaxHeightReached$.next(false);
  }

  @HostListener('window:resize', [])
  onWindowResize(): void {
    const containerHeight = this.scrollContainer.nativeElement.offsetHeight;
    const windowMaxHeight = window.innerHeight - 96*2;
    const result = containerHeight >= windowMaxHeight;
    this.isContainerMaxHeightReached$.next(result);
  }

  ngAfterViewInit(): void {
    this.resizeObserver = new ResizeObserver((entries) => {
      if (!this.isContainerMaxHeightReached) {
        for (let entry of entries) {
          const height = entry.contentRect.height;
          const result = height >= window.innerHeight - 96*2;
          this.isContainerMaxHeightReached$.next(result);
        }
      }
    });

    this.resizeObserver.observe(this.scrollContainer.nativeElement);
  }

  ngOnDestroy(): void {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  }

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
