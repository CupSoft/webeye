export interface IconsType {
  [key: string]: string
}

export type CardPropsType = {
  icon?: string;
  size?: string;
  title?: string;
  children?: string | React.ReactElement | never[];
  description?: string;
  bodyFlexStart?: boolean;
}