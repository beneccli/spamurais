import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-notification',
  imports: [],
  host: {
    'class': 'flex items-center last:mb-0 mb-2 px-6 py-4 bg-white dark:bg-zinc-700 rounded-md',
  },
  template: `
    <div class="w-12 h-12 mr-6 rounded bg-zinc-200 dark:bg-zinc-600"></div>
    <div class="flex-1 font-light">{{text}}</div>
  `,
})
export class NotificationComponent {
  @Input()
  text!: string;
}
