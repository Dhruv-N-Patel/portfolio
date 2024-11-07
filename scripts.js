document.addEventListener("DOMContentLoaded", function() {
    const runSimulationButton = document.querySelector(".run-simulation");
    const claimsCostImpact = document.querySelector(".summary-panel .summary-item:nth-child(1) span");
    const readmissionRateChange = document.querySelector(".summary-panel .summary-item:nth-child(2) span");
    const memberSatisfactionImpact = document.querySelector(".summary-panel .summary-item:nth-child(3) span");

    runSimulationButton.addEventListener("click", function() {
        // Example impact simulation (values would be dynamically generated in a real app)
        claimsCostImpact.textContent = "+8%";
        readmissionRateChange.textContent = "-3%";
        memberSatisfactionImpact.textContent = "+2%";
    });
});
