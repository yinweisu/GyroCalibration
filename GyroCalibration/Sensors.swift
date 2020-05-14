//
//  Sensors.swift
//  EdgeDetection
//
//  Created by Weisu Yin on 4/8/20.
//  Copyright © 2020 UCDavis. All rights reserved.
//

import Foundation
import CoreMotion
import os.log

class Sensors {
    let motionMgr = CMMotionManager()
    let updateInterval = 1.0 / 20.0
    var prevAttitude: CMAttitude?
    var prevTime: Date?
    
    init() {
    }
    
    // Raw data
    func startGyroscope() {
        if self.motionMgr.isGyroAvailable {
            self.motionMgr.gyroUpdateInterval = updateInterval
            self.motionMgr.startGyroUpdates()
            os_log("%@", type: .debug, "Gyroscope started with interval \(updateInterval)")
        } else {
            os_log("%@", type: .debug, "Gyroscope is not available on this device")
        }
    }
    
    // Raw data
    func startAccelerometer() {
        if self.motionMgr.isAccelerometerAvailable {
            self.motionMgr.accelerometerUpdateInterval = updateInterval
            self.motionMgr.startAccelerometerUpdates()
            os_log("%@", type: .debug, "Accelerometer started with interval \(updateInterval)")
        } else {
            os_log("%@", type: .debug, "Accelerometer is not available on this device")
        }
    }
    
    // Device motion encapsulate both gyroscope data and accelerometer data
    // It can also filter out gravity from accelerometer
    func startDeviceMotion() {
        if self.motionMgr.isDeviceMotionAvailable {
            self.motionMgr.deviceMotionUpdateInterval = updateInterval
            self.motionMgr.startDeviceMotionUpdates()
//            print(self.motionMgr.attitudeReferenceFrame)
            os_log("%@", type: .debug, "Device motion started with interval \(updateInterval)")
        } else {
            os_log("%@", type: .debug, "Device motion is not available on this device")
        }
    }
    
    func stopGyroscope() {
        if self.motionMgr.isGyroActive {
            self.motionMgr.stopGyroUpdates()
        }
    }
    
    func stopAccelerometer() {
        if self.motionMgr.isAccelerometerActive {
            self.motionMgr.stopAccelerometerUpdates()
        }
    }
    
    func stopDeviceMotion() {
        if self.motionMgr.isDeviceMotionActive {
            self.motionMgr.stopDeviceMotionUpdates()
        }
    }
    
    func getUnbiasedGyroscope() -> CMRotationRate? {
        return self.motionMgr.deviceMotion?.rotationRate
    }
    
    func getAttitude() -> CMAttitude? {
        return self.motionMgr.deviceMotion?.attitude
    }
    
    func getRotationRate() -> CMRotationRate? {
        return self.motionMgr.deviceMotion?.rotationRate
    }
    
    func getUserAcceleration() -> CMAcceleration? {
        return self.motionMgr.deviceMotion?.userAcceleration
    }
    
    func getRawGyroscope() -> CMRotationRate? {
        return self.motionMgr.gyroData?.rotationRate
    }
    
    func getRawAccelerometer() -> CMAcceleration? {
        return self.motionMgr.accelerometerData?.acceleration
    }
    
    func startGyroStreaming() {
        if self.motionMgr.isGyroAvailable {
            self.motionMgr.gyroUpdateInterval = 1.0 / 10.0
            self.motionMgr.startGyroUpdates(to: OperationQueue()) { (data, error) in
                guard let _ = data, error == nil else { return }
                if self.prevTime == nil {
                    self.prevTime = Date()
                } else {
                    let curTime = Date()
                    print(Float(curTime.timeIntervalSince(self.prevTime!)).avoidNotation)
                    self.prevTime = curTime
                }
            }
        }
    }
    
    func getChangeInAttitude() -> CMAttitude? {
        guard let prevAttitude = self.prevAttitude, let currentAttitude = self.motionMgr.deviceMotion?.attitude
            else {
                self.prevAttitude = self.motionMgr.deviceMotion?.attitude
                return nil }
//        self.prevAttitude = currentAttitude
//        print(prevAttitude, self.prevAttitude)
        let temp = currentAttitude
        currentAttitude.multiply(byInverseOf: prevAttitude)
//        print(temp, currentAttitude)
        return prevAttitude
    }
}
