import React from "react";

export type ButtonPropsType = React.ButtonHTMLAttributes<HTMLButtonElement> & React.ClassAttributes<HTMLButtonElement> & {
  btnType?: 'fill_purple' | 'purple' | 'yellow' | 'purple' | 'red' | 'green' | 'blue' | 'turquoise';
  size?: 'sm' | 'md' | 'lg';
  children: string | React.ReactElement;
  squared?: boolean;
  myClass?: string;
  noWrap?: boolean;
}