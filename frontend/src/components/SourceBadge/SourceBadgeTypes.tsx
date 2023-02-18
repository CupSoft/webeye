export type SourceCardPropsType = {
  state: 'ok' | 'partial' | 'critical' | string;
  rating: number;
  name: string;
  id: number;
  i: number;
}