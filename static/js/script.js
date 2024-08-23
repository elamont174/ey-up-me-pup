const editButtons = document.getElementsByClassName("btn-edit");
const userReviewText = document.getElementById("id_your_review");
const userReviewForm = document.getElementById("userReviewForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// ----- Edit button

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let userReviewId = e.target.getAttribute("user_review_id");
        let userReviewContent = document.getElementById(`userReview${userReviewId}`).innerText;
        userReviewText.value = userReviewContent;
        submitButton.innerText = "Update";
        userReviewForm.setAttribute("action", `edit_userReview/${userReviewId}`);
    });
}

// ----- Delete button

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let userReviewId = e.target.getAttribute("user_review_id");
        deleteConfirm.href = `delete_user_review/${userReviewId}`;
        deleteModal.show();
    });
}