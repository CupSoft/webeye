import { UseFormRegister } from 'react-hook-form'
import { FieldValues } from 'react-hook-form/dist/types'

type InputValidationOptions = {
  minLength?: number,
  maxLength?: number,
  required?: boolean,
  pattern?: RegExp
}
export type InputPropsType = React.InputHTMLAttributes<HTMLInputElement> & React.ClassAttributes<HTMLInputElement> & {
  options: InputValidationOptions,
  register: UseFormRegister<FieldValues>,
  name: string
}