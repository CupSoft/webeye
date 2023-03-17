import { useEffect } from "react";

type Event = MouseEvent | TouchEvent;

function useOnTouchOutside<T extends HTMLElement = HTMLElement>(
  ref: React.RefObject<T>,
  handler: (event: Event) => void,
) {
  useEffect(() => {
    const listener = (event: Event) => {
      const el = ref?.current

      if (!el) {
        return
      }

      if ('current' in el) {
        if ((el.current as HTMLElement).contains(event.target as Node)) {
          return
        }
      }

      handler(event)
    }

    document.addEventListener('mousedown', listener)
    document.addEventListener('touchstart', listener)

    return () => {
      document.removeEventListener('mousedown', listener)
      document.removeEventListener('touchstart', listener)
    }
  }, [ref, handler])
}

export default useOnTouchOutside