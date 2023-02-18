export type SourceCardPropsType = {
  state: 'ok' | 'partial' | 'critical' | string;
  rating: number;
  name: string;
  uuid: string;
  i: number;
}