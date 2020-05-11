const employeeListPrograms = document.querySelector(".e_name");
const isElement = (element) => {
  return element instanceof Element || element instanceof HTMLDocument;
};

const isInDOM = isElement(employeeListPrograms);
if (isInDOM === false) {
    const notInDoc = document.querySelector(".no_list");
    notInDoc.innerHTML = "There Are No Employees In This Program";
};
