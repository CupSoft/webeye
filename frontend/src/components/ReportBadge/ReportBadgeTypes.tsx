export type ReportBadgePropsType = {
  status: 'OK' | 'critical' | 'partial';
  is_moderated: boolean;
  text: string;
  created_at?: string;
  resource_name?: string;
  uuid: string;
  deleteClickHandler?: (evt: React.MouseEvent) => void;
  pacthClickHandler?: (evt: React.MouseEvent) => void;
  showModerated: boolean;
}