const label = document.getElementsByClassName("label");
const inputVisible = document.getElementsByClassName("inputVisible");
const inputHidden = document.getElementsByClassName("inputHidden");

inputHidden[0].addEventListener('input', () => {
        // const file = inputHidden[0].files;
        // if (file.lenght > 0) {
        //     inputVisible[0].value = file[0].name;
            console.log(inputHidden[0].files);
        }
    })

// for (let i = 0; i < 4; i++) {
//     inputHidden[i].addEventListener('input', () => {
//         const file = inputHidden[i].files;
//         if (file.lenght > 0) {
//             // inputVisible[i].value = file[0].name;
//             console.log(inputHidden[i]);
//         }
//     });
    // console.log(inputHidden[i]);
// }

// console.log(inputHidden[0]);

// inputHidden[0].addEventListener('input', () => {
//     console.log('ok');
// });
