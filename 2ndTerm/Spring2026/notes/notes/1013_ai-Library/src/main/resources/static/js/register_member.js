let idChecked = false;

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("checkIdBtn").addEventListener("click", function() {
        const m_id = document.getElementById("m_id").value.trim();
        if (m_id === "") {
            alert("아이디를 입력하세요.");
            retrun;
        }
        fetch("checkid?m_id=" + m_id)
            .then(res => res.text())
            .then(count => {
                if (count == 0) {
                    alert("사용 가능한 아이디입니다.");
                    idChecked = true;
                } else {
                    alert("이미 사용 중인 아이디입니다.");
                    idChecked = false;
                }
            });
    });

    document.getElementById("m_id").addEventListener("input", function() {
        idChecked = false;
    });

    document.querySelector("form").addEventListener("submit", function(e) {
        if (!idChecked) {
            e.preventDefault();
            alert("아이디 중복확인을 해주세요.")
        }
    });
});