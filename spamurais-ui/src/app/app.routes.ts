import { Routes } from '@angular/router';
import { AlertsComponent } from './pages/alerts.component';
import { ImportantComponent } from './pages/important.component';
import { ArchivedComponent } from './pages/archived.component';

export const routes: Routes = [
  { path: 'alerts', component: AlertsComponent },
  { path: 'important', component: ImportantComponent },
  { path: 'archived', component: ArchivedComponent },
];
