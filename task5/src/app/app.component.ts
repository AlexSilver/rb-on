import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

const STEP_SIZE = 5;
const LOWER_BOUND = 5;
const UPPER_BOUND = 90;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  imports: [CommonModule]
})
export class AppComponent {
  ballPosition = { top: 50, left: 50 };

  moveBall(direction: string) {
    switch (direction) {
      case 'up':
        if (this.ballPosition.top > LOWER_BOUND) this.ballPosition.top -= STEP_SIZE;
        break;
      case 'down':
        if (this.ballPosition.top < UPPER_BOUND) this.ballPosition.top += STEP_SIZE;
        break;
      case 'left':
        if (this.ballPosition.left > LOWER_BOUND) this.ballPosition.left -= STEP_SIZE;
        break;
      case 'right':
        if (this.ballPosition.left < UPPER_BOUND) this.ballPosition.left += STEP_SIZE;
        break;
    }
  }
}
