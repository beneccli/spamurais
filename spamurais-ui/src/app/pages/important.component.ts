import { Component } from '@angular/core';
import { NotificationComponent } from '../components/notification.component';

@Component({
  selector: 'app-important',
  imports: [NotificationComponent],
  template: `
    <div class="mx-8 mb-6">
      <h2 class="font-light mb-3">Today</h2>

      <div class="bg-zinc-100 dark:bg-zinc-800 p-2 rounded-lg">
        <app-notification text="Pegasus release expected on 12th December"></app-notification>
      </div>
      <h2 class="font-light my-3">Yesterday</h2>

      <div class="bg-zinc-100 dark:bg-zinc-800 p-2 rounded-lg">
        <app-notification text="Incident on Pegasus"></app-notification>
        <app-notification text="Training to be finished by 8th December"></app-notification>
      </div>
    </div>
  `,
})
export class ImportantComponent {

}
