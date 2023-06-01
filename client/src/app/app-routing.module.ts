import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { SigninComponent } from './signin/signin.component';
import { MilestoneFormComponent } from './milestone-form/milestone-form.component';
import { SignupComponent } from './signup/signup.component';
import { CampaignComponent } from './campaign/campaign.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'signin', component: SigninComponent },
  { path: 'milestone', component: MilestoneFormComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'campaign', component: CampaignComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
