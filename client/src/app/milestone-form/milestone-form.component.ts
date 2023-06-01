import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-milestone-form',
  templateUrl: './milestone-form.component.html',
  styleUrls: ['./milestone-form.component.css'],
})
export class MilestoneFormComponent {
  milestoneName: string = '';

  submitForm() {
    console.log('Submitted milestone name:', this.milestoneName);
    // Perform further actions with the milestone name
  }
}
