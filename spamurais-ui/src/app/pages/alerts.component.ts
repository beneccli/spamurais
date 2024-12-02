import { Component } from '@angular/core';
import { NotificationComponent } from '../components/notification.component';


@Component({
  selector: 'app-alerts',
  imports: [NotificationComponent],
  template: `
    <div class="mx-8 mb-6">
      <h2 class="font-light mb-3">Today</h2>

      <div class="bg-zinc-100 dark:bg-zinc-800 p-2 rounded-lg">
        <app-notification text="Update your password by end of week"></app-notification>
        <app-notification text="Report expected by end of month"></app-notification>
      </div>
    </div>
  `,
})
export class AlertsComponent {

}
