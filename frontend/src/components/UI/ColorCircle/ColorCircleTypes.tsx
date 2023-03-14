export type MoveIndicator = {
  x: number;
  y: number;
}

export type ColorCirclePropsType = {
  position: 'left' | 'right',
  color: 'yellow' | 'blue',
  moveIndicator: MoveIndicator
}