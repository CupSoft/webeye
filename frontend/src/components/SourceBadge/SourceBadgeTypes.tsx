export type SourceCardPropsType = {
  status: 'OK' | 'partial' | 'critical' | string;
  rating: number;
  name: string;
  uuid: string;
  i: number;
}