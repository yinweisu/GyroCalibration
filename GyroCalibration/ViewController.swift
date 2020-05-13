//
//  ViewController.swift
//  GyroCalibration
//
//  Created by Weisu Yin on 5/12/20.
//  Copyright © 2020 UCDavis. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    let sensors = Sensors()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        sensors.startGyroStreaming()
//        sensors.startGyroscope()
//        sensors.startDeviceMotion()
//        getRawGyro()
    }
    
    func getRawGyro() {
        let timer = Timer.scheduledTimer(withTimeInterval: 0.1, repeats: true) { (_) in
            guard let rotationRate = self.sensors.getRawGyroscope(), let calibratedRR = self.sensors.getUnbiasedGyroscope() else { return }
//            print("x: \(rotationRate.x), y: \(rotationRate.y), z:\(rotationRate.z)")
//            print("calibrated x: \(calibratedRR.x), calibrated y: \(calibratedRR.y), calibrated z: \(calibratedRR.z)")
            print("x calibration: \(Float(abs(rotationRate.x - calibratedRR.x)).avoidNotation), y calibration: \(Float(abs(rotationRate.y - calibratedRR.y)).avoidNotation), z calibration: \(Float(abs(rotationRate.z - calibratedRR.z)).avoidNotation)")
        }
    }
}

extension Formatter {
    static let avoidNotation: NumberFormatter = {
        let numberFormatter = NumberFormatter()
        numberFormatter.maximumFractionDigits = 20
        numberFormatter.numberStyle = .decimal
        return numberFormatter
    }()
}

extension FloatingPoint {
    var avoidNotation: String {
        return Formatter.avoidNotation.string(for: self) ?? ""
    }
}
