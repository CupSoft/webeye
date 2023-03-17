export type ReportBadgePropsType = {
  status: 'OK' | 'critical' | 'partial';
  is_moderated: boolean;
  text: string;
  created_at?: string;
  resource_name?: string;
}