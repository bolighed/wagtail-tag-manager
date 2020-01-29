import TagManager from "./tag_manager";

import { h } from "preact";
import { useState } from 'preact/hooks';

interface Props {
  manager: TagManager;
}

const CookieBar = (props: Props) => {
  const [value, setValue] = useState(0);

  return (
    <div className="inner">
      <p>
        This website uses cookies and other tracking technologies for
        functional and analytical purposes.
        To improve your browsing experience on our site,
        we would also like to place tracking cookies.
      </p>
    </div>
  )
}

export default CookieBar
