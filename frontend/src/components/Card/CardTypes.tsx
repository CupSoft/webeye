export interface IconsType {
  [key: string]: string
}

export type CardPropsType = {
  icon?: string;
  size?: string;
  title?: string | React.ReactElement;
  children?: string | React.ReactElement | never[];
  description?: string;
  bodyFlexStart?: boolean;
  scrolled?: boolean;
}